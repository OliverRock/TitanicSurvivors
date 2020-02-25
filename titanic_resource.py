from flask_restful import Resource, reqparse
from knn.knn_titanic import KNNTitanic


class Survivor(Resource):

    knntitanic = KNNTitanic()

    parser = reqparse.RequestParser()
    parser.add_argument('age')
    parser.add_argument('sex',
                        type=str)
    parser.add_argument('fare',
                        required=True
                        )

    def get(self):
        data = Survivor.parser.parse_args()
        result = Survivor.knntitanic.predict(data['age'], data['fare'], data['sex'])
        return {"You would..": result}, 200
