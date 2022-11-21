class NetworkDevicesController < ApplicationController
  def index
    @network_devices = NetworkDevice.all
  end

  def new
    @network_device = NetworkDevice.new
    render :new
  end

  def create
    @network_device = NetworkDevice.new(params.require(:network_device).permit(:mac_address, :name))
    @network_device.save!
    redirect_to network_devices_url
  end

  def destroy
    @network_device = NetworkDevice.find(params[:id])
    @network_device.destroy
    redirect_to network_devices_url
  end

  def show
    puts "tracking: #{params}"
  end
end
