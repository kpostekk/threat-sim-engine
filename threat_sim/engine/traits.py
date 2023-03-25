from enum import Enum


class NetworkEntityType(Enum):
    WORKSTATION = "workstation"
    SERVER = "server"
    ROUTER = "router"
    SWITCH = "switch"
    FIREWALL = "firewall"
    ACCESS_POINT = "access_point"
    LAPTOP = "laptop"
    PHONE = "phone"
    PRINTER = "printer"
    CCTV_IP_CAMERA = "cctv_ip_camera"
    SMART_TV = "smart_tv"
    SMART_APPLIANCE = "smart_appliance"


class EntityCurrentOS(Enum):
    WINDOWS = "windows"
    LINUX = "linux"
    MACOS = "macos"
    FREEBSD = "freebsd"
    ANDROID = "android"
    IOS = "ios"
    EMBEDDED = "embedded"


class EntityTraits(Enum):
    EOL = "eol"
    LEGACY_JAVA = "legacy_java"

