# fmt: off
#
#   # # # # # # # # # #
#   ว ง บ น * น ง ม ค ท
#   ย ม ก ด * ร ก ย ส ว
#
#       า เ  โ อ
#
# Note the unconventional steno order -- right side first left-to-right,
# then thumbs left-to-right, then left side right-to-left. This is according
# to the creator's design, since Thai has more complex onsets than codas.
KEYS = (
  "#",
  "น-", "ร-", "ง-", "ก-", "ม-", "ย-", "ค-", "ส-", "ท-", "ว-",
  "า-", "เ-",
  "*",
  "-โ", "-อ",
  "-น", "-ด", "-บ", "-ก", "-ง", "-ม", "-ว", "-ย"
)
# fmt: on

IMPLICIT_HYPHEN_KEYS = ("า-", "เ-", "*", "-โ", "-อ")
SUFFIX_KEYS = ()
NUMBER_KEY = "#"
NUMBERS = {
  "น-": "1-",
  "ง-": "2-",
  "ม-": "3-",
  "ค-": "4-",
  "โ-": "5-",
  "อ-": "-0",
  "-น": "6-",
  "-บ": "7-",
  "-ง": "8-",
  "-ว": "9-",
}
FERAL_NUMBER_KEY = False

UNDO_STROKE_STENO = "*"

ORTHOGRAPHY_RULES = []
ORTHOGRAPHY_RULES_ALIASES = {}
ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
  "Keyboard": {
    "#": ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"),
    "-ว": "q",
    "-ย": "a",
    "-ง": "w",
    "-ม": "s",
    "-บ": "e",
    "-ก": "d",
    "-น": "r",
    "-ด": "f",
    "า-": "c",
    "เ-": "v",
    "*": ("t", "g", "y", "h"),
    "-โ": "n",
    "-อ": "m",
    "น-": "u",
    "ร-": "j",
    "ง-": "i",
    "ก-": "k",
    "ม-": "o",
    "ย-": "l",
    "ค-": "p",
    "ส-": ";",
    "ท-": "[",
    "ว-": "'",
    "no-op": ("z", "x", "b", ",", ".", "/", "]", "\\"),
  },
  "Gemini PR": {
    # fmt: off
    "#": (
      "#1", "#2", "#3", "#4", "#5", "#6",
      "#7", "#8", "#9", "#A", "#B", "#C",
    ),
    # fmt: on
    "-ว": "S1-",
    "-ย": "S2-",
    "-ง": "T-",
    "-ม": "K-",
    "-บ": "P-",
    "-ก": "W-",
    "-น": "H-",
    "-ด": "R-",
    "า-": "A-",
    "เ-": "O-",
    "*": ("*1", "*2", "*3", "*4"),
    "-โ": "-E",
    "-อ": "-U",
    "น-": "-F",
    "ร-": "-R",
    "ง-": "-P",
    "ก-": "-B",
    "ม-": "-L",
    "ย-": "-G",
    "ค-": "-T",
    "ส-": "-S",
    "ท-": "-D",
    "ว-": "-Z",
    "no-op": ("Fn", "pwr", "res1", "res2"),
  },
}

DICTIONARIES_ROOT = "asset:StenoThaip:dictionaries"
DEFAULT_DICTIONARIES = []
