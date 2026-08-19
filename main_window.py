import customtkinter as ctk

from .dashboard import Dashboard
from .input_frame import InputFrame
from .result_frame import ResultFrame
from .database.db import Database
from .ml.predictor import PredictionEngine
from .utils.file_handler import append_prediction_csv


class ShoppingControlApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("dark-blue")

        self.title("AI Shopping Control Assistant")
        self.geometry("1120x720")
        self.minsize(1024, 680)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.database = Database()
        self.engine = PredictionEngine()

        self.input_frame = InputFrame(self, command=self.handle_predict)
        self.input_frame.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=14, pady=14)

        self.result_frame = ResultFrame(self)
        self.result_frame.grid(row=0, column=1, sticky="nsew", padx=(0, 14), pady=(14, 8))

        self.dashboard = Dashboard(self, self.database)
        self.dashboard.grid(row=1, column=1, sticky="nsew", padx=(0, 14), pady=(8, 14))

    def handle_predict(self, values):
        result = self.engine.predict(**values)
        self.result_frame.update_result(result)
        self.database.add_purchase(result["record"])
        append_prediction_csv(result["record"])
        self.dashboard.refresh()
