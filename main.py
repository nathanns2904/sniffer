from flask import Flask, jsonify, Response, request, json
from dbConfiguration import DbConnection as db

app = Flask(__name__)

@app.route('/')
@app.route('/<int:qty>/')
def homepage(qty=None):
    connection = db.getConnection()
    cursor = connection.cursor()

    try:
        str_quantity = '';
        if(qty != None and qty != 0):
            str_quantity = 'LIMIT ' + str(qty)
        else:
             str_quantity = 'LIMIT 100'

        cursor.execute('SELECT * FROM sniffer_log ' + str_quantity)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        itemsResult = []
        for item in result:
            content = {'id': item[0], 'sniffer': item[1], 'buffer': item[21], 'time': item[22]}
            itemsResult.append(content)
        return jsonify(itemsResult), 200
    except Exception as e:
        connection.close()
        cursor.close()
        return jsonify('Error when tried to get values'), 400

@app.route('/create', methods = ['POST'])
def create():
    body = request.get_json()
    try:
        if(body["sniffer_log_id"] == "" and body["sniffer"] == "" and body["cmd"] == "" and body["channel_sens"] == "" and body["rssi"] == ""
        and body["sequence_sniffer"] == "" and body["snr"] == "" and body["client"] == ""and body["sequence_msb"] == ""and body["sequence_lsb"] == ""and body["lora_boy"] == ""and body[" time"] == ""and body["latitude "] == ""and body["longitude "] == ""
        and body["precision_lat_lng"] == ""and body["bat"] == ""and body["rssi_client"] == ""and body["buffer"] == ""and body["timestamp"] == ""and body["gateway_id VALUES"] == "" ):
            return jsonify('Every properties must be inserted'), 401

        connection = db.getConnection()
        cursor = connection.cursor()

        sql = 'INSERT INTO sniffer_log_id, sniffer, cmd, channel_sens, rssi, sequence_sniffer, ' 
        'snr, client, sequence_msb, sequence_sens, sequence_lsb, lora_boy, time, latitude, longitude, '  
        'precision_lat_lng, bat, rssi_client, temperature_sens, humidity_sens, temperature_ext, buffer, timestamp, gateway_id VALUES ' 
        '( %s, %s, %s,  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s';

        val = ('sniffer_log_id', 'sniffer', 'cmd', 'channel_sens', 'rssi', 'sequence_sniffer', 'snr', 'client', 'sequence_msb',
        'sequence_sens', 'sequence_lsb', 'lora_boy', 'time', 'latitude', 'longitude', 'precision_lat_lng', 'bat',
        'rssi_client', 'temperature_sens', 'humidity_sens', 'temperature_ext', 'buffer', 'timestamp', 'gateway_id')

        cursor.execute(sql, val)
        cursor.commit()
        cursor.close()
        connection.close()

        return jsonify(body["name"])
    except Exception as e:
        return jsonify('Error when tried to create a temperacture'), 400      

if __name__ == "__main__":
    app.run(debug=True)

#app.run(host = '0.0.0.0')
