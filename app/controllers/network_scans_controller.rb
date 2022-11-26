class NetworkScansController < ApplicationController
  def index
  end

  def new
    strong_params = params.require(:network_scan).permit(:interface, :duration)
    interface     = strong_params[:interface]
    duration      = strong_params[:duration]

    cmd = "sudo ./bin/sniff.py -i #{interface} -d #{duration}"
    puts "running:'#{cmd}'"
    system(cmd)
    redirect_to network_devices_url
  end

  def rts
    render :rts
  end

  def rts_scan
    puts params
  end
end

