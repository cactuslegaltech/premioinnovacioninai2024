import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.PremioInnovacionINAI24',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description='Portales de Datos Personales\r\nEste repositorio contiene un conjunto de herramientas para la gestión de datos personales a través de dos portales: uno diseñado para el Titular de los datos y otro para el Responsable del tratamiento de dichos datos. A continuación, se detallan las características y pasos de implementación.\r\n\r\nCaracterísticas principales\r\n1. Portal para el Titular\r\nConsulta de avisos de privacidad: Ofrece dos opciones para revisar los avisos de privacidad de manera interactiva o consultando una inteligencia artificial (IA) entrenada con avisos de privacidad, la ley aplicable, y preguntas frecuentes.\r\nEjercicio de Derechos ARCO:\r\nExplicaciones sencillas y consultas a través de IA.\r\nSolicitud en línea con opción de firma electrónica.\r\nAlmacenamiento automático en la base de datos del Responsable.\r\nRecursos adicionales: Sección de preguntas frecuentes, generador gratuito de avisos de privacidad, y opciones de contacto.\r\n2. Portal para el Responsable\r\nBuzón de solicitudes de Derechos ARCO: Registro y seguimiento de solicitudes, integrando con Google Sheets.\r\nInteligencia Artificial: IA entrenada con normativa y preguntas frecuentes para ayudar en la gestión de los datos.\r\nConsultas rápidas: Desplegables para acceder fácilmente a la Ley Federal de Protección de Datos Personales (LFPDPPP) y avisos de privacidad.\r\nRequisitos técnicos\r\nPlataforma: Desarrollado en Docassemble, una plataforma de código abierto basada en Python.\r\nIA: Utiliza GPT-4-Turbo como motor principal de IA.\r\nIntegraciones: Soporta envío de correos automáticos mediante Sendgrid y almacenamiento de datos en Google Sheets o Excel.\r\nSeguridad: Encriptación automática y opción de autenticación multifactorial.\r\nCompatibilidad: Funciona en dispositivos móviles.\r\nInstalación\r\nInstalar Docassemble: Clonar el repositorio desde GitHub y seguir las instrucciones para instalar Docassemble Docassemble GitHub.\r\nConfigurar flujos: Importar y configurar los flujos para personalizarlos según las necesidades del Responsable.\r\nOpciones avanzadas: Si se requiere, se pueden modificar las integraciones (por ejemplo, cambiar Sendgrid o el almacenamiento en Google Sheets).\r\nContribuciones\r\nSe agradecen las contribuciones al proyecto. Puedes hacer un fork del repositorio, trabajar en tus modificaciones y luego crear un pull request para revisarlo.\r\n\r\nLicencia\r\nEste proyecto está disponible bajo la licencia de código abierto MIT.',
      long_description_content_type='text/markdown',
      author='diego flores',
      author_email='diego@cactuslegaltech.com',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/PremioInnovacionINAI24/', package='docassemble.PremioInnovacionINAI24'),
     )

