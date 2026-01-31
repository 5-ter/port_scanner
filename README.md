# Python Port Scanner

A simple and efficient command-line port scanner built with Python for scanning open ports on target machines.

## Features

- **Multiple Scan Modes**: Default common ports, full port range, or custom port ranges
- **IP Validation**: Validates IP address format before scanning
- **Smart Error Handling**: Distinguishes between closed ports, timeouts, and connection errors
- **Range Validation**: Automatically handles backwards ranges and validates port numbers (1-65535)
- **Graceful Fallbacks**: Falls back to default ports when invalid ranges are provided

## Requirements

- Python 3.x
- No external dependencies (uses built-in `socket` and `sys` modules)

## Installation

1. Clone or download the `port_scanner.py` file
2. Ensure Python 3.x is installed on your system
3. Run from command line

## Usage

```bash
python port_scanner.py <ip_address> [options]
```

### Options

- **No flags**: Scans default common ports (20, 21, 22, 23, 25, 53, 80, 443, 3306, 3389)
- `--full`: Scans all ports (1-65535)
- `--range <start> <end>`: Scans custom port range

## Examples

### Scan default common ports
```bash
python port_scanner.py 192.168.1.1
```

### Scan all ports (full scan)
```bash
python port_scanner.py 127.0.0.1 --full
```

### Scan custom port range
```bash
python port_scanner.py 192.168.1.1 --range 1 1000
```

### Scan with backwards range (automatically corrected)
```bash
python port_scanner.py 192.168.1.1 --range 1000 1
```

## Output

The scanner provides detailed feedback for each port:
- **"port X is open"**: Port is accepting connections
- **"Port X is closed"**: Port actively refused connection
- **"Port X failed to connect"**: Connection timed out (may be filtered)
- **"port X error: [details]"**: Other network errors

## How It Works

1. Validates the provided IP address format
2. Creates a TCP socket for each port in the scan range
3. Attempts to connect with a 2-second timeout
4. Reports the status of each port
5. Properly closes sockets after each attempt

## Planned Updates (v2.0)


- **Custom timeout time** (currently 5s)
- **Quiet Mode (`--quiet` or `-q`)**: Only display open ports, suppress closed/timeout messages
- **Improved Argument Handling**: Better parsing with help messages and more flexible flag combinations
- **Verbose Mode**: Additional details about the scanning process
- **Output Formatting**: Options for JSON or CSV output
- **Multi-threading**: Faster scanning with concurrent connections
- **Progress Indicator**: Show scanning progress for large port ranges

## Notes

- Scanning ports you don't own may be illegal in some jurisdictions
- This tool is intended for educational purposes and scanning your own systems
- Full port scans (1-65535) can take considerable time
- Some firewalls may block or rate-limit port scanning attempts

## Author

Created as a learning project for understanding network programming with Python sockets.

## License

Free to use for educational purposes.
