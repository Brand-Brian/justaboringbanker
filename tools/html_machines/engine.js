// Just a Boring Banker — shared machine engine
// Simulation helpers + a dependency-free canvas chart with hover + range slider.

const JBB = (() => {
  const fmt = n => "$" + Math.round(n).toLocaleString("en-CA");
  const pct = n => (n >= 0 ? "+" : "") + n.toFixed(2) + "%";

  const yearIndex = y => JBB_DATA.years.findIndex(r => r[0] === y);
  const minYear = () => JBB_DATA.years[0][0];
  const maxYear = () => JBB_DATA.years[JBB_DATA.years.length - 1][0];

  // Simulate one strategy across [fromY, toY].
  // profile: {eq, bd, gic} weights. monthly contributions are applied as 12x at year start.
  // withdrawStart/withdrawMonthly optional.
  function simulate(opts) {
    const { fromY, toY, start, monthly, profile, withdrawStart = null, withdrawMonthly = 0 } = opts;
    const out = { years: [], value: [], invested: [], withdrawn: [] };
    let value = start, invested = start, withdrawn = 0;
    for (let y = fromY; y <= toY; y++) {
      const row = JBB_DATA.years[yearIndex(y)];
      const contrib = (withdrawStart !== null && y >= withdrawStart) ? 0 : monthly * 12;
      value += contrib; invested += contrib;
      if (withdrawStart !== null && y >= withdrawStart) {
        const w = Math.min(value, withdrawMonthly * 12);
        value -= w; withdrawn += w;
      }
      const r = (profile.gic ? JBB_DATA.gicRate
        : (profile.eq * row[1] + profile.bd * row[2])) - (opts.fee || 0);
      value = Math.max(0, value * (1 + r / 100));
      out.years.push(y); out.value.push(value);
      out.invested.push(invested); out.withdrawn.push(withdrawn);
    }
    return out;
  }

  function annualized(finalV, invested, yearsCount) {
    if (invested <= 0 || yearsCount <= 0 || finalV <= 0) return 0;
    return (Math.pow(finalV / invested, 1 / yearsCount) - 1) * 100;
  }

  // ---- Chart ----
  function chart(canvas, tooltipEl) {
    const ctx = canvas.getContext("2d");
    const state = { series: [], years: [], panics: false, hoverX: null };

    function size() {
      const r = canvas.getBoundingClientRect();
      const dpr = window.devicePixelRatio || 1;
      canvas.width = r.width * dpr; canvas.height = r.height * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      return { w: r.width, h: r.height };
    }

    function draw() {
      const { w, h } = size();
      const P = { l: 10, r: 10, t: 12, b: 26 };
      ctx.clearRect(0, 0, w, h);
      const ys = state.years; if (!ys.length) return;
      const all = state.series.flatMap(s => s.data);
      const maxV = Math.max(...all, 1) * 1.06;
      const X = i => P.l + (i / Math.max(1, ys.length - 1)) * (w - P.l - P.r);
      const Y = v => h - P.b - (v / maxV) * (h - P.t - P.b);

      // panic shading
      if (state.panics) {
        ctx.fillStyle = "rgba(245, 213, 71, 0.22)";
        JBB_DATA.panics.forEach(p => {
          const a = ys.indexOf(p.from), b = ys.indexOf(p.to);
          if (a < 0 && b < 0) return;
          const x1 = X(Math.max(0, a)), x2 = X(b < 0 ? ys.length - 1 : b);
          ctx.fillRect(x1 - 4, P.t, (x2 - x1) + 8, h - P.t - P.b);
        });
      }
      // gridline baseline + year labels
      ctx.strokeStyle = "#d9e0da"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(P.l, h - P.b); ctx.lineTo(w - P.r, h - P.b); ctx.stroke();
      ctx.fillStyle = "#3d4f47"; ctx.font = "12px 'IBM Plex Sans', sans-serif";
      const step = Math.ceil(ys.length / Math.max(3, Math.floor(w / 90)));
      ys.forEach((y, i) => {
        if (i % step !== 0) return;
        const label = String(y), tw = ctx.measureText(label).width;
        // centre under the tick, but never let the first/last label run off the canvas
        const x = Math.min(Math.max(X(i) - tw / 2, 2), w - tw - 2);
        ctx.fillText(label, x, h - 8);
      });

      // series
      state.series.forEach(s => {
        ctx.strokeStyle = s.color; ctx.lineWidth = s.width || 2.5;
        if (s.dash) ctx.setLineDash(s.dash); else ctx.setLineDash([]);
        ctx.beginPath();
        s.data.forEach((v, i) => i ? ctx.lineTo(X(i), Y(v)) : ctx.moveTo(X(i), Y(v)));
        ctx.stroke(); ctx.setLineDash([]);
      });

      // hover crosshair
      if (state.hoverX !== null) {
        const i = Math.round(((state.hoverX - P.l) / (w - P.l - P.r)) * (ys.length - 1));
        if (i >= 0 && i < ys.length) {
          ctx.strokeStyle = "#10201a"; ctx.lineWidth = 1; ctx.setLineDash([4, 4]);
          ctx.beginPath(); ctx.moveTo(X(i), P.t); ctx.lineTo(X(i), h - P.b); ctx.stroke();
          ctx.setLineDash([]);
          if (tooltipEl) {
            tooltipEl.hidden = false;
            tooltipEl.style.left = Math.min(X(i) + 12, w - 190) + "px";
            tooltipEl.innerHTML = `<strong>${ys[i]}</strong>` + state.series
              .map(s => `<span><i style="background:${s.color}"></i>${s.name}: ${fmt(s.data[i])}</span>`).join("");
          }
        }
      } else if (tooltipEl) tooltipEl.hidden = true;
    }

    canvas.addEventListener("pointermove", e => {
      state.hoverX = e.offsetX; draw();
    });
    canvas.addEventListener("pointerleave", () => { state.hoverX = null; draw(); });
    canvas.addEventListener("pointercancel", () => { state.hoverX = null; draw(); });
    // touch has no "leave": clear the readout when the next tap lands off the chart
    document.addEventListener("pointerdown", e => {
      if (state.hoverX !== null && !canvas.contains(e.target)) { state.hoverX = null; draw(); }
    }, true);
    window.addEventListener("resize", draw);

    return {
      set(series, years, panics) { state.series = series; state.years = years; state.panics = panics; draw(); },
      redraw: draw
    };
  }

  // ---- Dual range window slider ----
  function rangeWindow(loEl, hiEl, labelEl, onChange) {
    const lo = () => Math.min(+loEl.value, +hiEl.value - 1);
    const hi = () => Math.max(+hiEl.value, +loEl.value + 1);
    function fire() {
      labelEl.textContent = lo() + " – " + hi();
      onChange(lo(), hi());
    }
    loEl.addEventListener("input", fire);
    hiEl.addEventListener("input", fire);
    return { fire, lo, hi, set(a, b) { loEl.value = a; hiEl.value = b; fire(); } };
  }

  // ---- Year-step animation ----
  function animator(stepFn, doneFn) {
    let timer = null;
    return {
      playing: () => !!timer,
      stop() { clearInterval(timer); timer = null; },
      play(speedMs = 220) {
        this.stop();
        timer = setInterval(() => { if (!stepFn()) { this.stop(); doneFn && doneFn(); } }, speedMs);
      }
    };
  }

  return { fmt, pct, simulate, annualized, chart, rangeWindow, animator, minYear, maxYear, yearIndex };
})();
