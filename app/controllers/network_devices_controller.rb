class NetworkDevicesController < ApplicationController
  def index
    @network_devices = NetworkDevice.all
    render json: @network_devices, adapter: :json
  end
end
