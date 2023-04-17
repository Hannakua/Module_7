from setuptools import setup

setup(
    name='clean20230417',
    version='0.3',
    description='Clean folder script',
    packages=['clean_folder'],
    license='MIT',
    author='Hanna',
    author_email='springcomes@gmail.com',
    install_requires=[],
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:cleanfunction']}
)




# У clean_folder/clean_folder/clean.py треба помістити все, що ми зробили на попередніх домашніх завданнях по розбору папки. 
# Ваше основнє завдання написати clean_folder/setup.py, щоб вбудований інструментарій Python міг встановити цей пакет та операційна 
# система могла використати цей пакет як консольну команду.

# Критерії прийому завдання
# Пакет встановлюється в систему командою pip install -e . (або python setup.py install, потрібні права адміністратора).
# Після установки в системі з'являється пакет clean_folder.
# Коли пакет встановлений в системі, скрипт можна викликати у будь-якому місці з консолі командою clean-folder
# Консольний скрипт обробляє аргументи командного рядка точно так, як і Python-скрипт.

# python -m pip install -e
