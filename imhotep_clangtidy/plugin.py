import os.path
import re

from imhotep.tools import Tool

class ClangTidy(Tool):
    # Example: /home/jerry/work/celcius-labs/tiny-http/src/http_router.h:1:9: warning: #pragma once in main file [clang-diagnostic-pragma-once-outside-header]
    response_format = re.compile(r'^(?P<filename>.*):(?P<line_number>\d+):\d+: (?P<message>.*)$')
    file_extensions = ('.cpp','.c','.cc',)

    def get_command(self, dirname, linter_configs=None):
        return 'clang-tidy'
