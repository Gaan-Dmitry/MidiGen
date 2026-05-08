import json
import random
from midiutil import MIDIFile

def create_midi_from_json(json_input, filename="output.mid"):
    try:
        data = json.loads(json_input)
        bpm = data.get("bpm", 120)
        notes = data.get("notes", [])

        # Создаем MIDI объект: 1 трек
        midi = MIDIFile(1)
        midi.addTempo(0, 0, bpm)

        for note in notes:
            # Элемент гуманизации (Humanize)
            v_rand = note['v'] + random.randint(-5, 5) # Вариация силы
            t_rand = note['t'] + random.uniform(-0.01, 0.01) # Вариация времени
            
            # Ограничиваем velocity в пределах MIDI стандарта
            v_final = max(0, min(127, v_rand))

            midi.addNote(
                track=0,
                channel=0,
                pitch=note['p'],
                time=t_rand,
                duration=note['d'],
                velocity=v_final
            )

        with open(filename, "wb") as out_file:
            midi.writeFile(out_file)
        
        return f"Успешно! Файл {filename} создан."
    
    except Exception as e:
        return f"Ошибка: {str(e)}"

# Пример использования (для тестов в консоли):
# if __name__ == "__main__":
#     test_json = '{"bpm": 120, "notes": [{"p": 60, "t": 0, "d": 1, "v": 80}]}'
#     print(create_midi_from_json(test_json))
