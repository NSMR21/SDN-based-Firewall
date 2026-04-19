from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.addresses import EthAddr, IPAddr

log = core.getLogger()

def _handle_ConnectionUp(event):
    log.info("Switch connected! Installing firewall rules...")

    # =========================
    # RULE 1: Block IP (h1)
    # =========================
    msg1 = of.ofp_flow_mod()
    msg1.priority = 100
    msg1.match.dl_type = 0x0800   # IPv4
    msg1.match.nw_src = IPAddr("10.0.0.1")
    event.connection.send(msg1)

    log.info("Blocking IP: 10.0.0.1")

    # =========================
    # RULE 2: Block MAC (h1)
    # =========================
    msg2 = of.ofp_flow_mod()
    msg2.priority = 100
    msg2.match.dl_src = EthAddr("00:00:00:00:00:01")
    event.connection.send(msg2)

    log.info("Blocking MAC: 00:00:00:00:00:01")

    # =========================
    # RULE 3: Block HTTP (Port 80)
    # =========================
    msg3 = of.ofp_flow_mod()
    msg3.priority = 100
    msg3.match.dl_type = 0x0800   # IPv4
    msg3.match.nw_proto = 6       # TCP
    msg3.match.tp_dst = 80
    event.connection.send(msg3)

    log.info("Blocking TCP Port 80 (HTTP)")

    # =========================
    # RULE 4: Default Allow (Flood)
    # =========================
    msg4 = of.ofp_flow_mod()
    msg4.priority = 0
    msg4.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg4)

    log.info("Default rule: Allow remaining traffic")

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
