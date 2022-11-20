class NetworkDevicesController < ApplicationController
  def index
    @network_devices = NetworkDevice.all
  end

  def show
    puts 'tracking'
  end
end
