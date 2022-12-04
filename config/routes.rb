Rails.application.routes.draw do
  root to: 'marit#index'

  # Network Devices
  delete '/network_devices/destroy_all', to: 'network_devices#destroy_all'
  resources :network_devices, only: [:index, :new, :create, :edit, :update, :show, :destroy]

  # Network Scans
  get '/network_scans/rts', to: 'network_scans#rts'
  post '/network_scans/rts', to: 'network_scans#rts_scan'
  resources :network_scans, only: [:index, :new, :edit]
end

