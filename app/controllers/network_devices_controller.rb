class NetworkDevicesController < ApplicationController
  def index
    @network_devices = NetworkDevice.all
    render json: @network_devices, each_serializer: NetworkDeviceSerializer, adapter: :json
  end
end
