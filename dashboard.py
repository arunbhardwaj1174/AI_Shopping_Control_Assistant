import customtkinter as ctk
from pathlib import Path

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from .utils.charts import build_summary_figure


class Dashboard(ctk.CTkFrame):
    def __init__(self, parent, database):
        super().__init__(parent)

        self.database = database
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        self.title_label.grid(row=0, column=0, sticky="w", padx=12, pady=(12, 4))

        self.summary_label = ctk.CTkLabel(
            self,
            text="Loading summary...",
            anchor="w",
            justify="left",
        )
        self.summary_label.grid(row=1, column=0, sticky="nsew", padx=12, pady=8)

        self.chart_container = ctk.CTkFrame(self)
        self.chart_container.grid(row=2, column=0, sticky="nsew", padx=12, pady=(0, 12))
        self.chart_container.grid_rowconfigure(0, weight=1)
        self.chart_container.grid_columnconfigure(0, weight=1)

        self.chart_canvas = None
        self.refresh()

    def refresh(self):
        summary = self.database.get_summary()
        self.summary_label.configure(
            text=(
                f"Total saved predictions: {summary['regret'] + summary['no_regret']}\n"
                f"Predicted regret cases: {summary['regret']}\n"
                f"Predicted non-regret cases: {summary['no_regret']}"
            )
        )
        self._draw_chart(summary)

    def _draw_chart(self, summary):
        if self.chart_canvas is not None:
            self.chart_canvas.get_tk_widget().destroy()

        figure = build_summary_figure(summary)
        self.chart_canvas = FigureCanvasTkAgg(figure, master=self.chart_container)
        self.chart_canvas.draw()
        self.chart_canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
