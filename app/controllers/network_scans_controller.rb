class NetworkScansController < ApplicationController
  def index
  end

  def new
    system("sudo ./bin/sniff.py")
    redirect_to network_devices_url
  end
end

