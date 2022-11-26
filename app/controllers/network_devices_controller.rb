class NetworkDevicesController < ApplicationController
  def index
    @network_devices = NetworkDevice.all
  end

  def new
    @network_device = NetworkDevice.new
    render :new
  end

  def edit
    @network_device = NetworkDevice.find(params[:id])
    render :edit
  end

  def update
    @network_device = NetworkDevice.find(params[:id])
    @network_device.update!(params.require(:network_device).permit(:name))
    redirect_to network_devices_url
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

  def destroy_all
    NetworkDevice.all.destroy_all
    redirect_to network_devices_url, status: 303
  end

  def show
    puts "tracking: #{params}"
  end
end

