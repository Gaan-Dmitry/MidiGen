import json
import random
from midiutil import MIDIFile
import customtkinter as ctk
from tkinter import messagebox, filedialog
import os


def create_midi_from_json(json_input, filename="output.mid"):
    """Конвертирует JSON с нотами в MIDI файл с гуманизацией."""
    try:
        data = json.loads(json_input)
        bpm = data.get("bpm", 120)
        notes = data.get("notes", [])

        # Создаем MIDI объект: 1 трек
        midi = MIDIFile(1)
        midi.addTempo(0, 0, bpm)

        for note in notes:
            # Элемент гуманизации (Humanize)
            v_rand = note['v'] + random.randint(-5, 5)  # Вариация силы +/- 5
            t_rand = note['t'] + random.uniform(-0.01, 0.01)  # Вариация времени +/- 0.01
            
            # Ограничиваем velocity в пределах MIDI стандарта (0-127)
            v_final = max(0, min(127, v_rand))

            midi.addNote(
                track=0,
                channel=0,
                pitch=note['p'],
                time=t_rand,
                duration=note['d'],
                volume=v_final
            )

        with open(filename, "wb") as out_file:
            midi.writeFile(out_file)
        
        return True, f"Успешно! Файл {filename} создан."
    
    except json.JSONDecodeError as e:
        return False, f"Ошибка JSON: {str(e)}"
    except KeyError as e:
        return False, f"Отсутствует обязательное поле: {str(e)}"
    except Exception as e:
        return False, f"Ошибка: {str(e)}"


class MIDIConverterApp(ctk.CTk):
    """Приложение для конвертации JSON нот в MIDI."""
    
    def __init__(self):
        super().__init__()
        
        # Настройки окна
        self.title("JSON to MIDI Converter")
        self.geometry("700x600")
        self.resizable(True, True)
        
        # Настройка сетки
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        # Заголовок
        self.title_label = ctk.CTkLabel(
            self, 
            text="Конвертер JSON нот в MIDI",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")
        
        # Текстовое поле для JSON
        self.json_label = ctk.CTkLabel(
            self,
            text='Вставьте JSON (формат: {"bpm": 120, "notes": [{"p": 60, "t": 0, "d": 1, "v": 80}, ...]})'
        )
        self.json_label.grid(row=1, column=0, padx=20, pady=(10, 5), sticky="ew")
        
        self.json_textbox = ctk.CTkTextbox(
            self,
            font=ctk.CTkFont(family="Courier", size=12),
            wrap="none"
        )
        self.json_textbox.grid(row=2, column=0, padx=20, pady=(5, 10), sticky="nsew")
        
        # Пример структуры
        example_json = '''{
  "bpm": 120,
  "notes": [
    {"p": 60, "t": 0, "d": 0.5, "v": 80},
    {"p": 64, "t": 0.5, "d": 0.5, "v": 75},
    {"p": 67, "t": 1.0, "d": 1.0, "v": 85}
  ]
}'''
        self.json_textbox.insert("0.0", example_json)
        
        # Фрейм для кнопок
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        self.button_frame.grid_columnconfigure((0, 1, 2), weight=1)
        
        # Кнопка конвертации
        self.convert_button = ctk.CTkButton(
            self.button_frame,
            text="Сконвертировать в MIDI",
            command=self.convert_to_midi,
            font=ctk.CTkFont(size=16, weight="bold"),
            height=40
        )
        self.convert_button.grid(row=0, column=0, padx=(0, 10), pady=5, sticky="ew")
        
        # Кнопка выбора пути сохранения
        self.save_path_label = ctk.CTkLabel(
            self.button_frame,
            text="Путь: ./output.mid"
        )
        self.save_path_label.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        
        self.browse_button = ctk.CTkButton(
            self.button_frame,
            text="Выбрать путь...",
            command=self.browse_save_path,
            height=30
        )
        self.browse_button.grid(row=0, column=2, padx=(10, 0), pady=5, sticky="ew")
        
        # Статус бар
        self.status_label = ctk.CTkLabel(
            self,
            text="Готов к работе",
            font=ctk.CTkFont(size=12),
            text_color="gray"
        )
        self.status_label.grid(row=4, column=0, padx=20, pady=(0, 20), sticky="ew")
        
        # Путь для сохранения по умолчанию
        self.save_path = "output.mid"
    
    def browse_save_path(self):
        """Открывает диалог выбора пути сохранения файла."""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".mid",
            filetypes=[("MIDI files", "*.mid"), ("All files", "*.*")],
            initialfile="output.mid",
            title="Сохранить MIDI файл как..."
        )
        if file_path:
            self.save_path = file_path
            self.save_path_label.configure(text=f"Путь: {file_path}")
    
    def convert_to_midi(self):
        """Обработчик кнопки конвертации."""
        json_input = self.json_textbox.get("0.0", "end").strip()
        
        if not json_input:
            messagebox.showwarning("Предупреждение", "Введите JSON данные!")
            return
        
        success, message = create_midi_from_json(json_input, self.save_path)
        
        if success:
            self.status_label.configure(text=message, text_color="green")
            messagebox.showinfo("Успех", message)
        else:
            self.status_label.configure(text=message, text_color="red")
            messagebox.showerror("Ошибка", message)


if __name__ == "__main__":
    # Установка темы
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    # Запуск приложения
    app = MIDIConverterApp()
    app.mainloop()
