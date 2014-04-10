namespace :db do
  desc "Drop all the projects"
  task empty: :environment do
    Project.destroy_all
    Project.reset_pk_sequence
  end
end