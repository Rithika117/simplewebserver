from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
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
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()