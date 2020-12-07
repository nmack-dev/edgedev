// Fetches API data on the click of a button
function fetchdata() {
    // The API URL
    const api_url = 'http://api.airvisual.com/v2/city?city=Cleveland&state=Ohio&country=USA&key=70ccf2c5-5531-4b1a-965d-fdfab0ba686d'

    // Gets data from the AirVisual API
    async function getapi(url)
    {
        const response = await fetch(url);

        var data = await response.json();
        console.log(data);
        show(data);
        postMQTT(data);
    }

    // Appends weather data to HTML table with every button click
    function show(data)
    {
        let td = data['data']['current']['weather'];
        let newData = [td.ts, td.tp, td.pr, td.hu, td.ws, td.wd];

        let tableRef = document.getElementById('environment');
        let newRow = tableRef.insertRow(1);

        for (let step = 0; step < 6; step++)
        {
            let newCell = newRow.insertCell(step);
            let newText = document.createTextNode(newData[step]);
            newCell.appendChild(newText);
        }
    }

    // Posts an MQTT message to the HTTP Server
    function postMQTT(data)
    {
        let td = data['data']['current']['weather'];
        msg = 'send_mqtt?';
        msg += 'topic=Weather';
        msg += '&'
        msg += 'message=' + td.ts;
        console.log(msg)
        fetch(msg, {method: 'POST'})
    }

    getapi(api_url)
}