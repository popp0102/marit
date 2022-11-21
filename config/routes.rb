Rails.application.routes.draw do
  root to: 'marit#index'
  resources :network_devices, only: [:index, :new, :create, :show, :destroy]
  resources :network_scans, only: [:index, :new]
end

