class NetworkScansController < ApplicationController
  def index
  end

  def new
    system("sudo ./bin/sniff.py")
  end
end

