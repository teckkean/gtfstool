#!/usr/bin/env python

from zipfile import ZipFile
import pandas as pd
import json
from pathlib import Path

# Load dtype from JSON
p = Path(__file__).with_name("dtype_gtfs.json")
with p.open("r") as read_file:
    dtype_gtfs = json.load(read_file)


def list_feed(filepath_zip_gtfs):
    """
    List all files in the GTFS Schedule ZIP file
    Parameters:
        filepath_zip_gtfs (str): Full file path of the GTFS Schedule Zip file including file name
    Returns:
        List of all files in the ZIP file
    """
    file_list = ZipFile(filepath_zip_gtfs).namelist()
    return file_list


"""
Below are functions to read individual GTFS Schedule file and return DataFrame.
Parameters:
    filepath_zip_gtfs (str): Full file path of the GTFS Schedule Zip file including file name.
Returns:
    DataFrame of the individual GTFS Schedule file.
"""


def read_agency(filepath_zip_gtfs):
    agency = pd.read_csv(
        ZipFile(filepath_zip_gtfs).open('agency.txt'),
        sep=',',
        dtype=dtype_gtfs)
    return agency


def read_routes(filepath_zip_gtfs):
    routes = pd.read_csv(
        ZipFile(filepath_zip_gtfs).open('routes.txt'),
        sep=',',
        dtype=dtype_gtfs)
    return routes


def read_trips(filepath_zip_gtfs):
    trips = pd.read_csv(
        ZipFile(filepath_zip_gtfs).open('trips.txt'),
        sep=',',
        dtype=dtype_gtfs)
    return trips


def read_stop_times(filepath_zip_gtfs):
    stop_times = pd.read_csv(
        ZipFile(filepath_zip_gtfs).open('stop_times.txt'),
        sep=',',
        dtype=dtype_gtfs)
    return stop_times


def read_stops(filepath_zip_gtfs):
    stops = pd.read_csv(
        ZipFile(filepath_zip_gtfs).open('stops.txt'),
        sep=',',
        dtype=dtype_gtfs)
    return stops


def read_shapes(filepath_zip_gtfs):
    shapes = pd.read_csv(
        ZipFile(filepath_zip_gtfs).open('shapes.txt'),
        sep=',',
        dtype=dtype_gtfs)
    return shapes


def read_calendar(filepath_zip_gtfs):
    calendar = pd.read_csv(
        ZipFile(filepath_zip_gtfs).open('calendar.txt'),
        sep=',',
        dtype=dtype_gtfs)
    return calendar


def read_calendar_dates(filepath_zip_gtfs):
    calendar_dates = pd.read_csv(
        ZipFile(filepath_zip_gtfs).open('calendar_dates.txt'),
        sep=',',
        dtype=dtype_gtfs)
    return calendar_dates


def read_notes(filepath_zip_gtfs):
    notes = pd.read_csv(
        ZipFile(filepath_zip_gtfs).open('notes.txt'),
        sep=',',
        dtype=dtype_gtfs)
    return notes


def read_feed_info(filepath_zip_gtfs):
    feed_info = pd.read_csv(
        ZipFile(filepath_zip_gtfs).open('feed_info.txt'),
        sep=',',
        dtype=dtype_gtfs)
    return feed_info
