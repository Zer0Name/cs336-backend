from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.OperatesRepo as OperatesRepo


def getOperatesForBar(bar):
    operatesRepo = OperatesRepo.OperatesRepo() 
    results = operatesRepo.getOperatesForBar(bar)
    return  jsonify([e.toJson() for e in results])