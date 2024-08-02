from flask import Flask, jsonify
import boto3

app = Flask(__name__)

# Initialize a session using Amazon S3
s3 = boto3.client('s3')
bucket_name = 'sectest-123'  # Hardcoded bucket name

def list_s3_contents(bucket_name, prefix=''):
    try:
        if prefix and not prefix.endswith('/'):
            prefix += '/'
        
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix, Delimiter='/')
        
        contents = []

        if 'CommonPrefixes' in response:
            directories = [common_prefix['Prefix'].rstrip('/') for common_prefix in response['CommonPrefixes']]
            contents.extend(directories)

        if 'Contents' in response:
            files = [content['Key'][len(prefix):] for content in response['Contents'] if content['Key'] != prefix]
            contents.extend(files)

        return contents
    except Exception as e:
        print(f"Error: {e}")
        return str(e)

@app.route('/list-bucket-content/', defaults={'path': ''})
@app.route('/list-bucket-content/<path:path>')
def list_bucket_content(path):
    contents = list_s3_contents(bucket_name, prefix=path)
    return jsonify({"content": contents})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

