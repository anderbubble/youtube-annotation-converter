#!/usr/bin/env python


from __future__ import print_function


import argparse
import dateutil.parser
import json
import sys
import xmltodict


SRT_FORMAT="{counter}\n{start} --> {end}\n{text}\n"
SRT_TIME_FORMAT='{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}'


def main ():
    parser = argparse.ArgumentParser()
    parser.add_argument('--json', type=int, default=None)
    args = parser.parse_args()

    annotations_document = xmltodict.parse(sys.stdin)
    annotations = annotations_document['document']['annotations']['annotation']

    if args.json is not None:
        print(json.dumps(annotations, indent=args.json), sys.stderr)

    for counter, annotation in enumerate(
            sorted(annotations, key=get_annotation_time), 1):
        text = annotation['TEXT']
        start = get_annotation_time(annotation, 0)
        end = get_annotation_time(annotation, 1)
        print(SRT_FORMAT.format(
            counter=counter,
            start=format_srt_time(start),
            end=format_srt_time(end),
            text=text,
        ))


def get_annotation_time (annotation, index=0):
    try:
        region = annotation['segment']['movingRegion']['rectRegion']
    except KeyError:
        region = annotation['segment']['movingRegion']['anchoredRegion']
    return dateutil.parser.parse(region[index]['@t'])


def format_srt_time (time_):
    return SRT_TIME_FORMAT.format(
        hours=time_.hour,
        minutes=time_.minute,
        seconds=time_.second,
        milliseconds=time_.microsecond / 1000,
    )


if __name__ == '__main__':
    main()
