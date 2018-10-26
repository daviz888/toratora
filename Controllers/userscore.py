import hashlib
import fileinput
import operator

from Shared.gameSettings import GameSettings


class UserScore:

    def __init__(self):
        self.__userScore = self.load()

    def get_users(self):
        return self.__userScore

    def load(self):
        users_score = []

        try:
            for line in fileinput.input(GameSettings.USER_DATA):
                name, score, md5 = line.split('[::]')
                md5 = md5.replace('\n', '')

                if str(hashlib.md5(str.encode(str(name + score + GameSettings.SALT))).hexdigest()) == str(md5):
                    users_score.append([str(name), int(score), str(md5)])

        except FileNotFoundError:
            print("empty list")

        users_score.sort(key=operator.itemgetter(1), reverse=True)
        users_score = users_score[0:11]

        return users_score

    def add_score(self, name, score):
        hash = hashlib.md5((str(name + str(score) + GameSettings.SALT)).encode('utf'))
        self.__userScore.append([name, str(score), hash.hexdigest()])

        with open(GameSettings.USER_DATA, "w") as user_file:
            for name, score, md5 in self.__userScore:
                user_file.write(str(name)+"[::]"+str(score)+"[::]"+str(md5)+"\n")
