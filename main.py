import tkinter.filedialog
import tkinter
import pyAesCrypt


def choose_file():
    filetypes = (("Текстовый файл", "*.txt"),)
    filename = tkinter.filedialog.askopenfilename(title="Открыть файл", initialdir="/", filetypes=filetypes)
    if filename:
        return filename


password = input('Введите пароль для шифрования файла: ')
try:
    file = choose_file()
    pyAesCrypt.encryptFile(file, f'{file}.aes', password)
    print('Шифрование успешно завершено!')
except:
    print('Файл не найден')
