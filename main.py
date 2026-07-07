from flask import Flask, request, jsonify
from datetime import datetime

posts = []

app = Flask(__name__)

@app.route('/posts', methods=['POST'])
def add_post():
    data = request.get_json()
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_post = {
        "id": len(posts) + 1,
        "title": data.get('title'),
        "content": data.get('content'),
        "category": data.get('category'),
        "tags": data.get('tags'),
        "createdAt": time
    }
    posts.append(new_post)
    return jsonify(new_post), 201

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    for p in posts:
        if p['id'] == post_id:
            data = request.get_json()
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if 'title' in data:
                p['title'] = data['title']
            if 'content' in data:
                p['content'] = data['content']
            if 'category' in data:
                p['category'] = data['category']
            if 'tags' in data:
                p['tags'] = data['tags']
            p['updatedAt'] = time
            return jsonify(p), 200
    return jsonify({"message": "Not Found"}), 404

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    for p in posts:
        if p['id'] == post_id:
            posts.remove(p)
            return '', 204
    return jsonify({"message": "Not Found"}), 404

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    for p in posts:
        if p['id'] == post_id:
            return jsonify(p), 200
    return jsonify({"message": "Not Found"}), 404

@app.route('/posts', methods=['GET'])
def get_posts():
    search = request.args.get('search') # query parameter 
    if search:
        filtered = [p for p in posts if search.lower() in p['title'].lower() or search.lower() in p['content'].lower()]
        return jsonify(filtered), 200
    return jsonify(posts), 200


if __name__ == '__main__':
    app.run(debug=True)