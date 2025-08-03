def ips_between(start: str, end: str) -> int:
    """
    Calculates the number of IPv4 addresses between two given addresses,
    including the first one and excluding the last one.

    Args:
        start: The starting IPv4 address as a string (e.g., "10.0.0.0").
        end: The ending IPv4 address as a string (e.g., "10.0.0.50").
             The last address will always be greater than the first one.

    Returns:
        The number of addresses between the two given IPs as an integer.
    """

    def _ipv4_to_int(ip_address_str: str) -> int:
        """
        Helper function to convert an IPv4 address string to its integer representation.
        """
        # Split the IP string into its four octets (parts)
        octets = list(map(int, ip_address_str.split('.')))
        
        # Calculate the integer value
        # Each octet contributes based on its position and powers of 256
        return (octets[0] * (256**3)) + \
               (octets[1] * (256**2)) + \
               (octets[2] * (256**1)) + \
               (octets[3] * (256**0))

    # Convert both start and end IP addresses to their integer forms
    start_int = _ipv4_to_int(start)
    end_int = _ipv4_to_int(end)

    # The difference between the integer representations gives the count
    return end_int - start_int