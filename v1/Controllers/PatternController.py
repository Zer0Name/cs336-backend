from flask import Flask, jsonify, Blueprint, request, json, make_response
import datetime

patternController = Blueprint('patternController', __name__)

import v1.Repos.PatternRepo as PatternRepo

@patternController.route('/1', methods=['GET'])
def pattern_1():
    patternRepo = PatternRepo.PatternRepo() 
    return str(patternRepo.pattern_1())

@patternController.route('/2', methods=['GET'])
def pattern_2():
    patternRepo = PatternRepo.PatternRepo() 
    return str(patternRepo.pattern_2())

@patternController.route('/3', methods=['GET'])
def pattern_3():
    patternRepo = PatternRepo.PatternRepo() 
    return str(patternRepo.pattern_3())

@patternController.route('/4', methods=['GET'])
def pattern_4():
    patternRepo = PatternRepo.PatternRepo() 
    return str(patternRepo.pattern_4())

@patternController.route('/5', methods=['GET'])
def pattern_5():
    patternRepo = PatternRepo.PatternRepo() 
    return str(patternRepo.pattern_5())