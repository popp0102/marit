class NetworkDevicesController < ApplicationController
  def index
    @network_devices = NetworkDevice.all
  end
end
