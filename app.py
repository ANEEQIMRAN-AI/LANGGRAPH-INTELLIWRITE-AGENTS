from flask import Flask, request, jsonify
from src_thesis_statement.main import run_thesis_generator
from src_essay_writer.main import run_essay_structurer
from src_paraphraser.main import run_paraphraser
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route("/thesis", methods=["POST"])
def thesis_generator():
    data = request.get_json()
    if not data or 'topic' not in data:
        return jsonify({"status": "error", "message": "Missing 'topic' in request body."}), 400
    try:
        raw_result = run_thesis_generator(data['topic'])
        lines = raw_result.strip().split("\n")
        thesis_list = [line.strip("0123456789. ").strip() for line in lines if line.strip()]
        return jsonify({
            "status": "success",
            "topic": data['topic'],
            "thesis_statements": thesis_list
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/essay", methods=["POST"])
def structured_essay():
    data = request.get_json()
    if not data or 'topic' not in data:
        return jsonify({"status": "error", "message": "Missing 'topic' in request body."}), 400
    try:
        result = run_essay_structurer(data['topic'])
        return jsonify({
            "status": "success",
            "topic": data['topic'],
            "structured_essay": result
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/paraphrase", methods=["POST"])
def paraphrase():
    data = request.get_json()
    if not data or 'paragraph' not in data:
        return jsonify({"status": "error", "message": "Missing 'paragraph' in request body."}), 400
    try:
        final_output = run_paraphraser(data['paragraph'])
        return jsonify({
            "status": "success",
            "original": data['paragraph'],
            "paraphrased": final_output
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 5002)), debug=True)
