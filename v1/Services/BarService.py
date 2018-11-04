from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.BarRepo as BarRepo


def getbarTopBeerBrand(day, dayOfWeek):
    barRepo = BarRepo.BarRepo()
    results = barRepo.getbarTopBeerBrand()
    return  jsonify([e.toJson() for e in results])