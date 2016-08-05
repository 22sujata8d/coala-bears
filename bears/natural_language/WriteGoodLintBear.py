from coalib.bearlib.abstractions.Linter import linter
from coalib.bears.requirements.NpmRequirement import NpmRequirement


@linter(executable='write-good',
        output_format='regex',
        output_regex=r'(?P<message>.*)\s*on\s*line\s*(?P<line>\d+)\s*at\scolumn'
                      '\s*(?P<column>\d+)'
        )
class WriteGoodLintBear:
    """
    Lints the text files using ``write-good`` for improving proses.

    See <https://github.com/btford/write-good> for more information.
    """
    LANGUAGES = {"Natural Language"}
    REQUIREMENTS = {NpmRequirement('write-good', '0.9.1')}
    AUTHORS = {'The coala developers'}
    AUTHORS_EMAILS = {'coala-devel@googlegroups.com'}
    LICENSE = 'AGPL-3.0'
    CAN_DETECT = {'Formatting', 'Grammar'}

    @staticmethod
    def create_arguments(filename, file, config_file,
                         allow_passive_voice: bool=False,
                         allow_so_beginning: bool=False,
                         allow_adverbs: bool=False,
                         allow_repeated_words: bool=False,
                         check_there_is: bool=False,
                         check_ambiguos_words: bool=False,
                         check_extra_words: bool=False,
                         check_cliche_exists: bool=False):
        """
        Using ``True`` will enable the check.

        :param allow_passive_voice:     Allows passive voice.
        :param allow_so_beginning:      Allows ``So`` at the beginning of
                                        the sentence.
        :param allow_adverbs:           Allows adverbs that can weaken the
                                        meaning, such as: ``really``, ``very``,
                                        ``extremely``, etc.
        :param allow_repeated_words:    Allows lexical illusions – cases
                                        where a word is repeated.
        :param check_there_is:          Checks for ``There is`` or ``There are``
                                        at the beginning of the sentence.
        :param check_ambiguos_words:    Checks for ``weasel words`` for example
                                        ``often``, ``probably``
        :param check_extra_words:       Checks for wordy phrases and
                                        unnecessary words.
        :param check_cliche_exists:     Checks for common cliche phrases in the
                                        sentence.
        """
        arg_map = {
            'allow_passive_voice': '--passive',
            'allow_so_beginning': '--so',
            'allow_adverbs': '--adverb',
            'allow_repeated_words': '--illusion',
            'check_there_is': '--thereIs',
            'check_ambiguos_words': '--weasel',
            'check_extra_words': '--tooWordy',
            'check_cliche_exists': '--cliches'
        }
        l = locals()
        args = tuple(arg for key, arg in arg_map.items()
                     if l[key])
        return args + (filename,)
