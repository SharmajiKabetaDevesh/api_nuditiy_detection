# from flask import Flask, request, jsonify
# from PIL import Image
# import numpy as np
# import io
# from nudenet import NudeClassifier
# from flask import Flask, render_template
# from flask_socketio import SocketIO, emit, send
# from PIL import Image
# from io import BytesIO
# import base64
# import os
# app = Flask(__name__)

# # Load your ML model here
# # Example:
# # from my_ml_model import classify_image
# # def classify_image(image):
# #     # Your classification code here
# #     return classification_result


# @app.route("/")
# def home():
#     return jsonify({"classification":12})
    
# app.route("/img" ,methods=["POST"])
# def output():
#     file=request.files['image']
#     img=Image.open(file.stream)
#     return jsonify({"msg":"success","size":[img.width,img.height]})

# # @app.route("/analyze", methods=["GET", "POST"])
# # def handle_image():
# #     if request.method == "GET":
# #         return "API is running"
# #     elif request.method == "POST":
# #         if 'image' not in request.files:
# #             return jsonify({"error": "No image provided"})

# #         image_data = request.files['image']
# #         try:
# #             classifier = NudeClassifier()
# #             pred = classifier.classify(image_data)
# #             print("Predictions:", pred)
# #             for file_path, inner_dict in pred.items():
# #                 unsafe_value = inner_dict.get('unsafe', 0.0)  
# #                 safe_value = inner_dict.get('safe', 0.0)  
# #                 print(f"Unsafe value: {unsafe_value}")
# #                 print(f"Safe value: {safe_value}")
# #                 if unsafe_value > 0.5:
# #                     return jsonify({"classification": unsafe_value})
# #                 else:
# #                     return jsonify({"classification": safe_value})
# #         except Exception as e:
# #             print(f"Error: {str(e)}")
# #             return jsonify({"error": "Error occurred during classification"})



# # @app.route("/analyze", methods=["GET", "POST"])
# # async def handle_image(image_data):
# #     if request.method == "GET":
# #         return "API is running"
# #     elif request.method == "POST":
# #         if 'image' not in request.files:
# #             return jsonify({"error": "No image provided"}), 400

# #     image_data = request.files['image']
# #     # imgin=image_data
# #     # decoded_image_data = base64.b64decode(imgin)
# #     # img=Image.open(BytesIO(decoded_image_data))
# #     # output_jpg=img.convert('RGB')
# #     img_path="static/"+image_data.filename
# #     image_data.save(img_path)
# #     current_directory = os.getcwd()
# #     # image_path = os.path.join(current_directory, 'desc.jpg')
# #     try:
# #         classifier = NudeClassifier()
# #         pred = classifier.classify(img_path)
# #         print("Predictions:", pred)
# #         for file_path, inner_dict in pred.items():
# #             unsafe_value = inner_dict.get('unsafe', 0.0)  
# #             safe_value = inner_dict.get('safe', 0.0)  
# #             print(f"Unsafe value: {unsafe_value}")
# #             print(f"Safe value: {safe_value}")
# #             if unsafe_value > 0.5:
# #                 return jsonify({"classification": unsafe_value})
# #             else:
# #                 return jsonify({"classification": safe_value})
# #     except Exception as e:
# #         print(f"Error: {str(e)}")
        
# #     finally:
# #         os.remove(img_path)
            

# @app.route("/analyze", methods=["GET", "POST"])
# async def handle_image():
#     if request.method == "GET":
#         return "API is running"
#     elif request.method == "POST":
#         if 'image' not in request.files:
#             return jsonify({"error": "No image provided"}), 400

#     image_data = request.files['image']
#     img_path="static/"+image_data.filename
#     image_data.save(img_path)
#     try:
#         classifier = NudeClassifier()
#         pred = classifier.classify(img_path)
#         for file_path, inner_dict in pred.items():
#             unsafe_value = inner_dict.get('unsafe', 0.0)  
#             safe_value = inner_dict.get('safe', 0.0)  
#             print(f"Unsafe value: {unsafe_value}")
#             print(f"Safe value: {safe_value}")
#             if unsafe_value > 0.5:
#                 return jsonify("True")
#             else:
#                 return jsonify("False")
#     except Exception as e:
#         print(f"Error: {str(e)}")
#     finally:
#         os.remove(img_path)
           

# if __name__ == "__main__":
#     app.run(debug=True, port=3001)
from flask import Flask, request, jsonify
from nudenet import NudeClassifier
import os
import asyncio

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify("Api is running")


@app.route("/analyze", methods=["GET", "POST"])
async def handle_image():
    if request.method == "GET":
        return "API is running"
    elif request.method == "POST":
        if 'image' not in request.files:
            return jsonify({"error": "No image provided"}), 400
        image_data = request.files['image']
        img_path = "static/" + image_data.filename
        image_data.save(img_path)
        try:
            classifier = NudeClassifier()
            pred =  classifier.classify(img_path)
            for file_path, inner_dict in pred.items():
                unsafe_value = inner_dict.get('unsafe', 0.0)
                safe_value = inner_dict.get('safe', 0.0)
                print(f"Unsafe value: {unsafe_value}")
                print(f"Safe value: {safe_value}")
                if unsafe_value > 0.5:
                    return jsonify("true")
                else:
                    return jsonify("false")
        except Exception as e:
            print(f"Error: {str(e)}")
        finally:
            os.remove(img_path)



@app.route('/print_phone_number', methods=['POST'])
def print_phone_number():
    phone_number = request.json.get('phone_number')
    if phone_number:
        print("Received phone number:", phone_number)
        return "Phone number received and printed successfully."
    else:
        return "Phone number not found in request.", 400

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(app.run(debug=True,host="192.168.194.19", port=3001))
    loop.run_forever
   
    
   
