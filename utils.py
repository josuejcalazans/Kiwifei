import os
import re
from datetime import datetime


def alexandria_ascii_art():
  alexandria = r"""
     _  ___          _  __      _ 
    | |/ (_)_      _(_)/ _| ___(_)
    | ' /| \ \ /\ / / | |_ / _ \ |
    | . \| |\ V  V /| |  _|  __/ |
    |_|\_\_| \_/\_/ |_|_|  \___|_|
    
  Author: YdzpXDs | Alex4ndria Team
  Community: https://t.me/+DoZ_EeKWN0NhY2Ix
  Script: {name}
  Version: {version}
  """
  print(alexandria.format(name='kiwifei', version='Alpha 0.1'))


def clear_screen():
  os.system('cls || clear')


def create_folder(folder_name):
  path = os.path.join(os.getcwd(), folder_name)

  if not os.path.exists(path):
    os.mkdir(path)

  return path


def clear_folder_name(name):
  sanitized_name = re.sub(r'[<>:"/\\|?*]', ' ', name)
  sanitized_name = re.sub(r'\s+', ' ', sanitized_name)
  sanitized_name = re.sub(r'\.+$', '', sanitized_name)
  return sanitized_name.strip()


def shorten_folder_name(full_path, max_length=245):
  if len(full_path) <= max_length:
    return full_path
  directory, file_name = os.path.split(full_path)
  base_name, extension = os.path.splitext(file_name)
  base_name = base_name[:max_length - len(directory) - len(extension) - 1]
  return os.path.join(directory, base_name + extension)


def log_to_file(filename, message):
  timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  with open(filename, 'a', encoding='UTF-8') as file:
    file.write(f'{timestamp} - {message}\n')


def logger(message, error=None, warning=None):
  if error:
    log_to_file('hotm4rtei_erros.txt', message)
  if warning:
    log_to_file('hotm4rtei_avisos.txt', message)


class SilentLogger(object):
  def __init__(self, url=None, output_path=None):
    self.url = url
    self.output_path = output_path

  def debug(self, msg):
    pass

  def warning(self, msg):
    logger(f"WARNING: {msg} - URL: {self.url}, Path: {self.output_path}")

  def error(self, msg):
    logger(f"ERROR: {msg} - URL: {self.url}, Path: {self.output_path}")