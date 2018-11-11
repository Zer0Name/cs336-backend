from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.LikesRepo as LikesRepo

def getAllLikes():
    likesRepo = LikesRepo.LikesRepo() 
    results = likesRepo.getAllLikes()
    return  jsonify([e.toJson() for e in results])

'''
checks to make:
no duplicate entries
drinker exists
beer exists
'''
def insertLikes(likes):
	likesRepo = LikesRepo.LikesRepo()
	return likesRepo.insertLikes(likes)

'''
checks to make:
no duplicate entries
drinker exists
beer exists
'''
def updateLikes(likes,oldDrinker, oldBeer):
	likesRepo = LikesRepo.LikesRepo()
	return likesRepo.updateLikes(likes, oldDrinker, oldBeer)

''' no check cascade should be handled by table '''
def deleteLikes(likes):
	likesRepo = LikesRepo.LikesRepo()
	return likesRepo.deleteLikes(likes)
    