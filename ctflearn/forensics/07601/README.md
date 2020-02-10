# 07601

## Figuring out whats in the file

This challenge provides a link to a file called AGT.png. I attempted to open
it, which failed. A quick look with the GNU file utility shows its actually
a JPEG. Ok so switch the file extension and open it. Its a weird America's Got
Talent image. Not much interesting.

## Look at the binary data

I ran `strings` on the file and found what looked like file paths. Such as
`__MACOS/Secret Stuff/Don't Open This/...`. Do a quick google search and find
out that JPEG files can be used as zip archives (found this out from a small
business blog encouraging business people to use this method to send data
around. Oh lord why...).

## Open it up

On a hunch, I just ran `unzip` on the JPEG... it worked. Now I have a file
`__MACOS/Secret Stuff/Don't Open This/I Warned You.jpeg`. Run strings on this
and grep for `CTF` and bam, there's the flag.

## Rating
The problem is listed as medium. I would say it runs closer to easy but did
require knowledge of what tools to use and a lesser known JPEG trick.
