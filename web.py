from http.server import BaseHTTPRequestHandler, HTTPServer

# HTML content for TCP/IP Protocols
content = '''
<html>
<head>
    <title>TCP/IP Protocol Suite</title>
</head>
<body>

    <h2>TCP/IP Protocol Suite</h2>

    <table border="1">
        <tr>
            <th>Layer</th>
            <th>Protocols</th>
        </tr>
        <tr>
            <td>Application Layer</td>
            <td>HTTP, HTTPS, FTP, SMTP, DNS, DHCP, Telnet, SNMP</td>
        </tr>
        <tr>
            <td>Transport Layer</td>
            <td>TCP, UDP</td>
        </tr>
        <tr>
            <td>Internet Layer</td>
            <td>IP, ICMP, ARP, IGMP</td>
        </tr>
        <tr>
            <td>Network Access Layer</td>
            <td>Ethernet, Wi-Fi, PPP</td>
        </tr>
    </table>

</body>
</html>
'''

# Define the request handler
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode())

# Main server code
if __name__ == "__main__":
    print("This is my TCP/IP protocols webserver")
    server_address = ('', 8000)  # Bind to localhost at port 8000
    httpd = HTTPServer(server_address, MyServer)
    httpd.serve_forever()
