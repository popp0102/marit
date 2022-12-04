class NetworkScansController < ApplicationController
  def index
  end

  def new
    strong_params = params.require(:network_scan).permit(:interface, :duration, :mac_address)
    interface     = strong_params[:interface]
    duration      = (strong_params[:duration].to_i <= 0) ? 10 : strong_params[:duration]
    mac_address   = strong_params[:mac_address]

    cmd = "sudo ./bin/sniff.py -i #{interface} -d #{duration}"
    cmd += " -m #{mac_address}" if mac_address.present?

    puts "running:'#{cmd}'"
    system(cmd)
    redirect_to network_devices_url
  end

  def edit
    @network_device = NetworkDevice.find(params[:id])
    render :index
  end

  def rts
    @network_device = NetworkDevice.find(params[:id])
    render :rts
  end

  def rts_scan
    strong_params = params.require(:network_scan).permit(:spoofed_mac, :target_mac, :duration)
    target_mac    = strong_params[:target_mac]
    duration      = (strong_params[:duration].to_i <= 0) ? 1 : strong_params[:duration]
    spoofed_mac   = (strong_params[:spoofed_mac] == '') ? '11:22:33:44:55:66' : strong_params[:spoofed_mac]

    @network_device = NetworkDevice.find_by(mac_address: target_mac)

    cmd = "sudo ./bin/rts_cts.py -i #{@network_device.interface} -s #{spoofed_mac} -t #{target_mac} -d #{duration}"
    puts "running:'#{cmd}'"

    system(cmd)
    redirect_to network_devices_url
  end
end

