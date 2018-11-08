from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.FrequentsRepo as FrequentsRepo

'''
checks to make:
no duplicate entries
drinker exists
bar exists
drinker and bar in the same state
'''
def insertFrequents(frequents):
	frequentsRepo = FrequentsRepo.FrequentsRepo()
	return frequentsRepo.insertFrequents(frequents)

'''
checks to make:
no duplicate entries
drinker exists
bar exists
drinker and bar in the same state
'''
def updateFrequents(frequents,oldDrinker, oldBar):
	frequentsRepo = FrequentsRepo.FrequentsRepo()
	return frequentsRepo.updateFrequents(frequents, oldDrinker, oldBar)

''' no check cascade should be handled by table '''
def deleteFrequents(frequents):
	frequentsRepo = FrequentsRepo.FrequentsRepo()
	return frequentsRepo.deleteFrequents(frequents)