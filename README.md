# YouTube annotation converter

YouTube is disabling annotations support, and removing all existing
annotations[1].

[1]: https://support.google.com/youtube/answer/7342737

However, I really like this Mr. Gimmick Annotated NES Longplay by
Frank Cifaldi:

- https://www.youtube.com/watch?v=zYcf2yUgblc
- https://www.youtube.com/watch?v=BzsA3ziEIuQ
- https://www.youtube.com/watch?v=DoznFNKFM1E
- https://www.youtube.com/watch?v=0QH_pdDy95Q

In an effort to preserve the annotated experience without flattening the data into a single rendered video, I wrote this script to convert the YouTube XML data to another format[2].

[2]: https://en.wikipedia.org/wiki/SubRip

I used Stefan Sundin's annotation copier[3] to retrieve the original
annotation data in XML format.

[3]: https://stefansundin.github.io/youtube-copy-annotations/
