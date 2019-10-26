"""
https://www.hackerrank.com/challenges/basic-cryptanalysis
"""
from collections import defaultdict, OrderedDict

ALPHA = "abcdefghijklmnopqrstuvwxyz"

facts = {}    # encoded_char: original_char
results = OrderedDict()


def update_results_and_facts(encoded_word, original_word_string=None):
    if original_word_string is None:
        results[encoded_word.raw] = "".join([facts[c] for c in encoded_word.raw])
    else:
        results[encoded_word.raw] = original_word_string
        for i in range(len(encoded_word.raw)):
            facts[encoded_word.raw[i]] = original_word_string[i]


def can_identify_all_chars(word):
    """Check if all characters in `word` can be identified already."""
    for c in word:
        if facts.get(c) is None:
            return False
    return True


def get_pattern(word):
    raw, mapping, pattern = list(ALPHA), {}, ""
    for c in word:
        if c not in facts:
            facts[c] = None
        if c not in mapping:
            mapping[c] = raw.pop(0)
        pattern += mapping[c]
    return pattern


def find_closest_from_same_pattern(encoded_word, dictionary_words_with_same_pattern):
    result = defaultdict(list)

    # Matched all chars we know, use "?" for those we don't
    curr_str = "".join(["?" if facts.get(c) is None else facts.get(c) for c in encoded_word.raw])

    for original_word in dictionary_words_with_same_pattern:
        matched_cnt = 0
        for i in range(len(curr_str)):
            if curr_str[i] == original_word.raw[i]:
                matched_cnt += 1
        result[matched_cnt].append(original_word)

    max_matched_cnt = max(result.keys())
    #print(f"{curr_str} vs {[x.raw for x in result[max_matched_cnt]]}")
    if len(result[max_matched_cnt]) == 1:
        # This must be it!
        update_results_and_facts(encoded_word, result[max_matched_cnt][0].raw)
    # else, more than one dictionary words have the same matched-char counts, guess again later


class Word:
    def __init__(self, word):
        self.raw = word
        self.pattern = get_pattern(word)


def func(dictionary_words, input):
    dictionary_map = defaultdict(list)
    for word in dictionary_words:
        dictionary_map[len(word)].append(Word(word))

    encoded_map = defaultdict(list)
    for word in [s.strip().lower() for s in input.split(" ")]:
        encoded_map[len(word)].append(Word(word))
        results[word] = None

    # Check from the longest words (rarer) first
    max_len = min(max(dictionary_map.keys()), max(encoded_map.keys()))
    
    for word_len in range(max_len, 1, -1):
        for encoded_word in encoded_map[word_len]:
            if can_identify_all_chars(encoded_word.raw) is True:
                update_results_and_facts(encoded_word)
            else:
                # Find all words in dictionary with the same pattern
                dictionary_words_with_same_pattern = [
                    d_word for d_word in dictionary_map[word_len] if encoded_word.pattern == d_word.pattern]

                if len(dictionary_words_with_same_pattern) == 1:
                    # Found only one match, so this must be it
                    update_results_and_facts(encoded_word, original_word_string=dictionary_words_with_same_pattern[0].raw)
                else:
                    # Find the closest match with the same pattern
                    find_closest_from_same_pattern(encoded_word, dictionary_words_with_same_pattern)

    # Final check to see if any encoded words previously having more than one dictionary words with the same
    # matched-char counts
    for k, v in results.items():
        if v is None:
            results[k] = "".join([facts[c] for c in k])

    return " ".join(results.values())


def main():
    with open("dictionary.lst", "r") as f:
        d = f.readlines()
    d = [w.strip().lower() for w in d]
    func(d, s)


# Test case 1
sample_dict = ["afaik", "afaiks", "ai", "aids", "aidses", "ais", "ansi", "ansis", "ascii", "asciis", "ada", "adas", "amiga", "basic", "basics", "bbs", "bbses", "bitnet", "bitnets", "blt", "blts", "bsd", "bsds", "borg", "borgs", "cobol", "cobols", "cs", "ddt", "ddts", "dec", "deced", "decing", "decs", "dp", "dps", "datamation", "datamations", "dilbert", "dilberts", "english", "englishes", "eris", "erises", "faq", "faqs", "fm", "fms", "fud", "fuds", "gigo", "guido", "ibm", "imho", "internet", "internets", "java", "knuth", "knuths", "ks", "linus", "linux", "linuxes", "mego", "megos", "mips", "mipses", "mars", "marses", "microsoft", "multics", "multicses", "news", "newses", "os", "oses", "otoh", "parc", "parcs", "pd", "pm", "pmed", "pming", "pms", "pascal", "pascals", "pentium", "pentiums", "perl", "perls", "python", "qwerty", "rfc", "rfcs", "rtfm", "rtfmed", "rtfming", "rtfms", "so", "sos", "soses", "sos", "sun", "suns", "telnet", "telnetted", "telnetting", "telnets", "tex", "texes", "url", "urls", "unix", "unixes", "usenet", "usenets", "vax", "vaxes", "wysiwyg", "winchester", "winchesters", "xes", "ymmv", "abbrev", "abbrevs", "accumulator", "accumulators", "acolyte", "acolytes", "admin", "admins", "alt", "alts", "amoeba", "amoebae", "amoebas", "app", "apps", "arena", "arenas", "asbestos", "atomic", "avatar", "avatars", "backgammon", "background", "backgrounds", "bandwidth", "bandwidths", "bang", "bangs", "banner", "banners", "bar", "barf", "barfed", "barfing", "barfs", "barn", "barney", "barneys", "barns", "baroque", "bars", "batch", "baud", "bauds", "bazaar", "bazaars", "beam", "beamed", "beaming", "beams", "beep", "beeps", "benchmark", "benchmarks", "beta", "betas", "bible", "bibles", "biff", "biffed", "biffing", "biffs", "bigot", "bigots", "bit", "bits", "blast", "blasted", "blasting", "blasts", "blat", "blats", "blink", "blinked", "blinking", "blinks", "blivet", "blivets", "block", "blocked", "blocking", "blocks", "boa", "board", "boards", "boas", "bob", "bobs", "bogus", "boink", "boinked", "boinking", "boinks", "bomb", "bombed", "bombing", "bombs", "boot", "booted", "booting", "boots", "bot", "bounce", "bounced", "bounces", "bouncing", "boustrophedon", "boustrophedons", "box", "boxen", "boxes", "break", "breaking", "breaks", "brittle", "brittler", "brittlest", "broke", "broken", "browser", "browsers", "bug", "bugs", "bulletproof", "bum", "bummed", "bumming", "bump", "bumped", "bumping", "bumps", "bums", "burble", "burbled", "burbles", "burbling", "buzz", "buzzed", "buzzes", "buzzing", "byte", "bytes", "calculator", "calculators", "can", "canned", "canning", "canonical", "cans", "cascade", "cascades", "cat", "catatonic", "cathedral", "cathedrals", "cats", "catted", "catting", "chad", "chads", "chain", "chained", "chaining", "chains", "channel", "channels", "char", "chars", "check", "checks", "cheerfully", "chemist", "chemists", "choke", "choked", "chokes", "choking", "chomp", "chomped", "chomper", "chompers", "chomping", "chomps", "chrome", "chromes", "chug", "chugged", "chugging", "chugs", "clean", "cleaned", "cleaner", "cleanest", "cleaning", "cleans", "clobber", "clobbered", "clobbering", "clobbers", "clock", "clocked", "clocking", "clocks", "clone", "cloned", "clones", "cloning", "coaster", "coasters", "code", "codes", "compact", "compacter", "compactest", "compo", "compos", "compress", "compressed", "compresses", "compressing", "con", "condom", "condoms", "confuser", "confusers", "cons", "consed", "conses", "consing", "console", "consoles", "cookbook", "cookbooks", "cookie", "cookies", "copper", "coppers", "core", "cores", "cowboy", "cowboys", "cracker", "crackers", "cracking", "crackings", "crank", "cranked", "cranking", "cranks", "crash", "crashed", "crashes", "crashing", "cray", "crayola", "crayolas", "crayon", "crayons", "crays", "creationism", "creationisms", "creep", "creeping", "creeps", "crept", "cretin", "cretinous", "cretins", "crippleware", "cripplewares", "crock", "crocks", "crumb", "crumbs", "crunch", "crunched", "crunches", "crunching", "cube", "cubes", "cubing", "cubinged", "cubinging", "cubings", "cyberpunk", "cyberpunks", "cyberspace", "cyberspaces", "cycle", "cycled", "cycles", "cycling", "daemon", "daemons", "dd", "dded", "dding", "dds", "dead", "deader", "deadest", "deadlock", "deadlocks", "decay", "decays", "deckle", "deckles", "defenestration", "defenestrations", "delta", "deltas", "demented", "demigod", "demigods", "demo", "demoed", "demoing", "demon", "demons", "demos", "deprecated", "diddle", "diddled", "diddles", "diddling", "die", "died", "dies", "diff", "diffed", "diffing", "diffs", "digit", "digits", "dike", "diked", "dikes", "diking", "ding", "dings", "dink", "dinker", "dinkest", "dinosaur", "dinosaurs", "disclaimer", "disclaimers", "distribution", "distributions", "doc", "docs", "documentation", "documentations", "dodgier", "dodgiest", "dodgy", "dongle", "dongles", "donuts", "donutses", "doorstop", "doorstops", "down", "downed", "downing", "download", "downloaded", "downloading", "downloads", "downs", "dragon", "dragons", "drain", "drained", "draining", "drains", "driver", "drivers", "droid", "droids", "drone", "drones", "drugged", "drum", "drums", "dump", "dumps", "dying", "earthquake", "earthquakes", "echo", "echoes", "echos", "ed", "eds", "elegant", "elephantine", "elite", "elvish", "elvishes", "email", "emailed", "emailing", "emails", "emoticon", "emoticons", "empire", "empires", "engine", "engines", "enhancement", "enhancements", "epoch", "epochs", "epsilon", "epsilons", "erotics", "eroticses", "evil", "eviler", "evilest", "eviller", "evillest", "excl", "excls", "exec", "execked", "execking", "execs", "exploit", "exploits", "factor", "factors", "fairings", "fairingses", "fan", "fans", "faradize", "faradized", "faradizes", "faradizing", "farming", "farmings", "fascist", "faultier", "faultiest", "faulty", "feature", "features", "fence", "fences", "filter", "filters", "fine", "finer", "finest", "finger", "fingered", "fingering", "fingers", "firefighting", "firefightings", "firmware", "firmwares", "fish", "fishes", "fix", "fixes", "flag", "flags", "flakier", "flakiest", "flaky", "flame", "flamed", "flamer", "flamers", "flames", "flaming", "flap", "flapped", "flapping", "flaps", "flat", "flatten", "flattened", "flattening", "flattens", "flatter", "flattest", "flavor", "flavorful", "flavors", "flippies", "flippy", "flood", "flooded", "flooding", "floods", "flowchart", "flowcharts", "flush", "flushed", "flushes", "flushing", "flytrap", "flytraps", "followup", "followups", "foo", "fool", "fools", "footprint", "footprints", "fora", "foreground", "foregrounded", "foregrounding", "foregrounds", "forked", "forum", "forums", "fossil", "fossils", "frag", "fragile", "fragiler", "fragilest", "frags", "freeware", "freewares", "freeze", "freezes", "freezing", "fried", "fries", "frog", "frogging", "frogginged", "frogginging", "froggings", "frogs", "froze", "frozen", "fry", "frying", "fudge", "fudged", "fudges", "fudging", "fum", "fums", "funkier", "funkiest", "funky", "fuzzball", "fuzzballs", "gag", "gagged", "gagging", "gags", "gas", "gaseous", "gases", "gassed", "gasses", "gassing", "gen", "generate", "generated", "generates", "generating", "gens", "gig", "gigs", "gillion", "gillions", "glass", "glasses", "glitch", "glitched", "glitches", "glitching", "glob", "globed", "globing", "globs", "glue", "glues", "gnarlier", "gnarliest", "gnarly", "gobble", "gobbled", "gobbles", "gobbling", "golden", "goldener", "goldenest", "gonk", "gonked", "gonking", "gonks", "gonzo", "gopher", "gophers", "gorp", "gorps", "gotcha", "gotchas", "gribble", "gribbles", "grind", "grinding", "grinds", "grok", "grokked", "grokking", "groks", "ground", "grovel", "groveled", "groveling", "grovelled", "grovelling", "grovels", "grue", "grues", "grunge", "grunges", "gun", "gunned", "gunning", "guns", "guru", "gurus", "hack", "hacked", "hacker", "hackers", "hacking", "hacks", "hair", "hairball", "hairballs", "hairier", "hairiest", "hairs", "hairy", "hammer", "hammered", "hammering", "hammers", "hamster", "hamsters", "handle", "handles", "handshaking", "handshakings", "hang", "hanged", "hanging", "hangs", "happily", "hardwired", "hat", "hats", "heartbeat", "heartbeats", "heavyweight", "hex", "hexadecimal", "hexadecimals", "hexes", "highly", "hing", "hings", "hirsute", "hoarding", "hoardings", "hobbit", "hobbits", "hog", "hogs", "hole", "holes", "hook", "hooks", "hop", "hopped", "hopping", "hops", "hose", "hosed", "hoses", "hosing", "hotlink", "hotlinks", "huff", "huffed", "huffing", "huffs", "hung", "hyperspace", "hyperspaces", "ice", "ices", "idempotent", "inc", "incantation", "incantations", "inced", "incing", "include", "included", "includes", "including", "incs", "infinite", "infinities", "infinity", "inflate", "inflated", "inflates", "inflating", "interesting", "interrupt", "interrupts", "intro", "intros", "iron", "ironmonger", "ironmongers", "irons", "jaggies", "jaggieses", "jello", "jellos", "jiffies", "jiffy", "jock", "jocks", "kahuna", "kahunas", "ken", "kens", "kick", "kicked", "kicking", "kicks", "kit", "kits", "kludge", "kludged", "kludges", "kludging", "kluge", "kluged", "kluges", "kluging", "knobs", "koan", "koans", "lag", "lags", "lamer", "lamers", "lase", "lased", "lases", "lasing", "laundromat", "laundromats", "leak", "leaks", "leech", "leeches", "legal", "legalese", "legaleses", "letterbomb", "letterbombs", "life", "lightweight", "lint", "linted", "linting", "lints", "live", "liver", "lives", "livest", "liveware", "livewares", "lobotomies", "lobotomy", "logical", "lose", "loser", "losers", "loses", "losing", "loss", "losses", "lost", "lurker", "lurkers", "machinable", "macro", "macrologies", "macrology", "macros", "magic", "magics", "mailbomb", "mailbombed", "mailbombing", "mailbombs", "mainframe", "mainframes", "management", "managements", "manged", "mangeds", "mangle", "mangled", "mangler", "manglers", "mangles", "mangling", "marbles", "marginal", "marginally", "martian", "martians", "massage", "massaged", "massages", "massaging", "meg", "megs", "meme", "memes", "meta", "mickey", "mickeys", "microfloppies", "microfloppieses", "minifloppies", "minifloppieses", "misfeature", "misfeatures", "mockingbird", "mockingbirds", "mod", "modded", "modding", "mode", "modes", "mods", "modulo", "monstrosities", "monstrosity", "mu", "multitask", "multitasks", "mumble", "munch", "munched", "munches", "munching", "munchkin", "munchkins", "mundane", "mundanes", "mung", "munged", "munging", "mungs", "music", "musics", "mutter", "muttered", "muttering", "mutters", "naive", "naiver", "naivest", "nanobot", "nanobots", "nanotechnologies", "nanotechnology", "nature", "natures", "neophilia", "neophilias", "nerd", "nerds", "netiquette", "netiquettes", "netter", "netters", "newbie", "newbies", "newsgroup", "newsgroups", "nick", "nickle", "nickles", "nicks", "noddy", "node", "nodes", "nonlinear", "nontrivial", "notwork", "notworks", "nude", "nuder", "nudest", "nuke", "nuked", "nukes", "nuking", "numbers", "numberses", "nybble", "nybbled", "nybbles", "nybbling", "nyetwork", "nyetworks", "obscure", "obscurer", "obscurest", "offline", "op", "open", "opens", "ops", "optimism", "optimisms", "orphan", "orphans", "orthogonal", "overrun", "overruns", "parse", "parsed", "parses", "parsing", "pastie", "pasties", "patch", "patched", "patches", "patching", "path", "pathological", "paths", "payware", "paywares", "peek", "peeks", "peon", "peons", "pessimal", "pessimaled", "pessimaling", "pessimals", "phage", "phages", "phase", "phases", "phreaking", "phreakings", "ping", "pinged", "pinging", "pings", "pipe", "pipes", "pistol", "pistols", "playpen", "playpens", "plonk", "plonked", "plonking", "plonks", "plumbing", "plumbings", "pod", "pods", "poke", "pokes", "poll", "polled", "polling", "polls", "pop", "popped", "popping", "pops", "poser", "posers", "post", "posted", "posting", "postings", "postmaster", "postmasters", "posts", "priesthood", "priesthoods", "print", "printed", "printing", "prints", "profile", "profiles", "program", "programming", "programmings", "programs", "proprietary", "protocol", "protocols", "prowler", "prowlers", "pseudo", "pseudos", "puff", "puffed", "puffing", "puffs", "punt", "punted", "punting", "punts", "push", "pushed", "pushes", "pushing", "quad", "quads", "quantifiers", "quarter", "quarters", "ques", "queses", "quine", "quines", "quotient", "quotients", "random", "randomness", "randomnesses", "randoms", "rape", "raped", "rapes", "raping", "rave", "raved", "raves", "raving", "real", "realer", "realest", "reaper", "reapers", "recursion", "recursions", "replicator", "replicators", "replies", "reply", "restriction", "restrictions", "rip", "ripoff", "ripoffs", "ripped", "ripping", "rips", "roach", "roached", "roaches", "roaching", "robot", "robots", "robust", "robuster", "robustest", "rococo", "rogue", "rogues", "root", "roots", "rude", "ruder", "rudest", "runes", "runic", "sacred", "saga", "sagas", "said", "salt", "salts", "samizdat", "samizdats", "samurai", "samurais", "sandbox", "sandboxes", "say", "saying", "says", "scag", "scagged", "scagging", "scags", "scratch", "scratched", "scratches", "scratching", "screen", "screens", "screw", "screws", "scribble", "scribbles", "scrog", "scrogged", "scrogging", "scrogs", "segment", "segmented", "segmenting", "segments", "selvage", "selvages", "semi", "semis", "server", "servers", "shareware", "sharewares", "shebang", "shebangs", "shell", "shells", "shim", "shims", "showstopper", "showstoppers", "shriek", "shrieks", "sidecar", "sidecars", "silicon", "silicons", "silo", "silos", "skulker", "skulkers", "slab", "slabbed", "slabbing", "slabs", "slack", "slacks", "slash", "slashes", "sleep", "sleeping", "sleeps", "slept", "slim", "slims", "slop", "slops", "slurp", "slurped", "slurping", "slurps", "smart", "smarter", "smartest", "smiley", "smileys", "smoke", "smoked", "smokes", "smoking", "smurf", "smurfs", "snail", "snailed", "snailing", "snails", "snap", "snapped", "snapping", "snaps", "snarf", "snarfed", "snarfing", "snarfs", "snark", "snarks", "sneaker", "sneakers", "sniff", "sniffed", "sniffing", "sniffs", "softies", "softy", "spam", "spammed", "spamming", "spams", "spangle", "spangles", "spawn", "spawns", "speedometer", "speedometers", "spell", "spells", "spiffier", "spiffiest", "spiffy", "spike", "spiked", "spikes", "spiking", "spin", "spinning", "spins", "splat", "splats", "spoiler", "spoilers", "sponge", "sponges", "spoof", "spoofed", "spoofing", "spoofs", "spool", "spooled", "spooling", "spools", "spun", "stack", "stacks", "state", "states", "stoppage", "stoppages", "store", "stores", "stroke", "strokes", "strudel", "strudels", "studlier", "studliest", "studly", "stunning", "suit", "suits", "sunspots", "sunspotses", "support", "supports", "surf", "surfed", "surfing", "surfs", "swab", "swabbed", "swabbing", "swabs", "swap", "swapped", "swapping", "swaps", "swizzle", "swizzled", "swizzles", "swizzling", "sync", "syncs", "sysop", "sysops", "system", "systems", "tanked", "taste", "tastes", "tee", "tees", "tense", "tenser", "tensest", "tentacle", "tentacles", "test", "tests", "text", "texts", "theologies", "theology", "theories", "theory", "thrash", "thrashed", "thrashes", "thrashing", "thread", "threads", "thud", "thuds", "thumb", "thumbs", "thunk", "thunks", "tick", "ticks", "toad", "toadded", "toadding", "toads", "toast", "toasted", "toaster", "toasters", "toasting", "toasts", "toggle", "toggled", "toggles", "toggling", "tool", "tooled", "tooling", "tools", "tourist", "touristic", "tourists", "toy", "toys", "trampoline", "trampolines", "trap", "trapped", "trapping", "traps", "trash", "trashed", "trashes", "trashing", "trawl", "trawled", "trawling", "trawls", "trivial", "troglodyte", "troglodytes", "troll", "trolled", "trolling", "trolls", "tron", "tronned", "tronning", "trons", "tube", "tubes", "tune", "tuned", "tunes", "tuning", "tweak", "tweaked", "tweaking", "tweaks", "tweeter", "tweeters", "twiddle", "twiddled", "twiddles", "twiddling", "twink", "twinks", "uninteresting", "up", "upload", "uploaded", "uploading", "uploads", "upped", "upping", "ups", "urchin", "urchins", "user", "users", "vanilla", "vaporware", "vaporwares", "var", "vars", "verbiage", "verbiages", "videotex", "videotexes", "virgin", "virtual", "virus", "viruses", "visionaries", "visionary", "voice", "voiced", "voices", "voicing", "wabbit", "wabbits", "waldo", "waldoes", "waldos", "walk", "walks", "wall", "walled", "walling", "wallpaper", "wallpapers", "walls", "wank", "wanked", "wanking", "wanks", "wannabee", "wannabees", "warez", "warezes", "wart", "warts", "weasel", "weasels", "wedged", "wedgie", "wedgies", "weeds", "weedses", "weenie", "weenies", "wetware", "wetwares", "whack", "whacked", "whacker", "whackers", "whacking", "whacks", "whales", "whaleses", "wheel", "wheels", "widget", "widgets", "wiggles", "wiggleses", "win", "winner", "winners", "winning", "wins", "wired", "wireds", "wizard", "wizardly", "wizards", "womble", "wombles", "won", "wonkier", "wonkiest", "wonky", "woofer", "woofers", "workaround", "workarounds", "worm", "wormhole", "wormholes", "worms", "zap", "zapped", "zapping", "zaps", "zen", "zenned", "zenning", "zens", "zero", "zeroed", "zeroes", "zeroing", "zeros", "zeroth", "zigamorph", "zigamorphs", "zip", "zipped", "zipping", "zips", "zombie", "zombies", "zorch", "zorched", "zorches", "zorching"]

sample_input = "lhpohes gvjhe ztytwojmmtel lgsfcgver segpsltjyl vftstelc djfl rml catrroel jscvjqjyfo mjlesl lcjmmfqe egvj gsfyhtyq sjfgver csfaotyq lfxtyq gjywplesl lxljm dxcel mpyctyq ztytwojmmtelel mfcgv spres mjm psgvty bfml ofle mjlc dtc tygfycfctjy dfsyl zpygvel csfao yealqsjpml atyl lgsjql qyfsotelc fseyf ojllel gjzmselltyq wpyhtelc zpltgl weygel afyher rstnesl aefleo rtyhes mvflel yphe rstnes qojder dtwwer lojml mfcgvel reocfl djzder djpygtyq gstmmoeafsel reg cpdel qspyqe mflctel csflvtyq vfcl avfghtyq vftsdfool mzer rsjye wjjol psol mplvtyq catrroe mvfqe lgseey leqzeycer wjseqsjpyrer lmjtoes msjwtoel docl djpyger cjpstlcl goefy gojddesl mjrl qjddoe gjy gpdtyql lyftotyq rjayojfr swgl vjle atrqec gjzmfgces frfl qotcgver gspzd zftodjzdl lyfsh"

expected_output = "skulker choke minifloppies scratched recursions hairiest boas dps twiddles orthogonal posers stoppage echo cranking roached trawling saying confusers sysop bytes punting minifloppieses patch ruder pop urchin zaps lase post bit incantation barns munches trawl newsgroups wins scrogs gnarliest arena losses compressing funkiest musics fences wanked drivers weasel dinker phases nuke driver globed biffed slops patches deltas bombed bouncing cripplewares dec tubes grunge pasties trashing hats whacking hairballs pmed drone fools urls pushing twiddle phage screen segmented foregrounded spoiler profiles blts bounced tourists clean clobbers pods gobble con cubings snailing download rfcs hose widget compacter adas glitched crumb mailbombs snark"

assert func(sample_dict, sample_input) == expected_output
