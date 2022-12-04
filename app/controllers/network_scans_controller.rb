class NetworkScansController < ApplicationController
  def index
  end

  def new
    strong_params = params.require(:network_scan).permit(:interface, :duration, :mac_address)
    interface     = strong_params[:interface]
    duration      = strong_params[:duration].to_i
    duration      = (duration <= 0) ? 10 : duration
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
    render :rts
  end

  def rts_scan
    puts params
  end
end

