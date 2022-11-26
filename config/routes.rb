Rails.application.routes.draw do
  root to: 'marit#index'
  delete '/network_devices/destroy_all', to: 'network_devices#destroy_all'
  resources :network_devices, only: [:index, :new, :create, :edit, :update, :show, :destroy]
  resources :network_scans, only: [:index, :new]
end

