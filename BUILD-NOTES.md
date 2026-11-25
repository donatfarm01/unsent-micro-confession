# Build notes — Unsent: The Micro-Confession Sprint

The entry is a single program, main.py, written from the bounty rules. It writes one two-part micro-confession to the output entry file: a To line naming who the message was meant for, and the unsent message itself on one line, exactly as typed, with nothing after it.

The confession was chosen against the judge's brief, in the order the brief weighs things. First, the two-part form is exact: a To line, then one message line, no explanation. Second, the reason it stayed in drafts is felt rather than stated: a small weekly ritual, setting a plate for a father who is gone, kept secret from the mother it would hurt to tell. The words are specific and honest, a concrete habit rather than a general feeling. Third, the To line and the message need each other: the person who must not know is the person the message is addressed to, and swapping the addressee would break the confession. Fourth, it reads as typed and never sent, not as something written to be sent: there is no joke, no greeting, and no motivational turn.

The program checks its own output against the gate before writing: the whole entry must be between one and two hundred sixty characters, and the message line at most two hundred characters. The entry as written is ninety three characters in total with an eighty five character message line, so both limits hold with room to spare.

Verification was done by running the program locally and reading the output file back, counting its characters, and computing its hash. The kit check was run from the kit directory against this repository, and its result is recorded in the build report.
