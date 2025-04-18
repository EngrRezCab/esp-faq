# -*- coding: utf-8 -*-
#
# English Language RTD & Sphinx config file
#
# Uses ../conf_common.py for most non-language-specific settings.

# Importing conf_common adds all the non-language-specific
# parts to this conf module
try:
    from conf_common import *  # noqa: F403,F401
except ImportError:
    import os
    import sys
    sys.path.insert(0, os.path.abspath('../'))
    from conf_common import *

import datetime

current_year = datetime.datetime.now().year

# General information about the project.
project = u'ESP-FAQ'
copyright = u'2020 - {}, 乐鑫信息科技（上海）股份有限公司'.format(current_year)
pdf_title = u'ESP-FAQ 手册'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'zh_CN'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'ReadtheDocsTemplate.tex', project,
   copyright, 'manual'),
]

html_js_files += ['js/chatbot_widget_cn.js']
